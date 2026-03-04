import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const discover = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/discover' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number(),
    icon: z.string().default('📄'),
  }),
});

const define = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/define' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number(),
    icon: z.string().default('📄'),
  }),
});

const design = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/design' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number(),
    icon: z.string().default('📄'),
  }),
});

const refine = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/refine' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number(),
    icon: z.string().default('📄'),
  }),
});

const deliver = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/deliver' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number(),
    icon: z.string().default('📄'),
  }),
});

export const collections = { discover, define, design, refine, deliver };
