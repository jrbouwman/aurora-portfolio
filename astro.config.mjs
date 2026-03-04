// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://jrbouwman.github.io',
  base: '/aurora-portfolio',
  vite: {
    plugins: [tailwindcss()]
  }
});
