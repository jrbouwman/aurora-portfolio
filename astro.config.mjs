// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://your-username.github.io',
  // Uncomment and set if deploying to a subpath (e.g., /aurora-portfolio):
  // base: '/aurora-portfolio',
  vite: {
    plugins: [tailwindcss()]
  }
});
