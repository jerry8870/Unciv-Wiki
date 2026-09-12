import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { docsLoader, i18nLoader } from '@astrojs/starlight/loaders';
import { docsSchema, i18nSchema } from '@astrojs/starlight/schema';
import { withBase } from './site';

const schema = docsSchema({ extend: z.object({
  indexable: z.boolean().default(true),
  gameVersion: z.string().optional(),
  appBuild: z.number().optional(),
  ruleset: z.string().optional(),
  sources: z.array(z.string()).default([]),
  publishedAt: z.coerce.date().optional(),
  lastUpdated: z.union([z.boolean(), z.coerce.date()]).optional(),
  article: z.boolean().default(false),
}) });

export const collections = {
  i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
  docs: defineCollection({ loader: docsLoader(), schema: (context) => schema(context).transform((data) => ({
    ...data,
    pagefind: data.indexable && data.pagefind,
    sidebar: { ...data.sidebar, hidden: !data.indexable || data.sidebar.hidden },
    hero: data.hero && { ...data.hero, actions: data.hero.actions?.map((action) => ({ ...action, link: withBase(action.link) })) },
  })) }),
};
