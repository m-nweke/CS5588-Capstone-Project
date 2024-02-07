import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from "path";
import childProcess from 'child_process';

// git describe
const getCommitHash = () => {
  try {
    const proc = childProcess.execSync('git describe --always');
    const resp = proc.toString('utf-8').trim();
    return JSON.stringify(resp);
  } catch (_) {
    return JSON.stringify('development');
  }
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  define: {
    '__APP_VERSION__': getCommitHash(),
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
      '~animate.css': path.resolve(__dirname, 'node_modules/animate.css'),
      '~nprogress': path.resolve(__dirname, 'node_modules/nprogress'),
    }
  }
})
