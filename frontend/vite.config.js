import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import yaml from 'vite-plugin-yaml2';

export default defineConfig({
	plugins: [sveltekit(),yaml()]
});
