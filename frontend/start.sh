#!/bin/bash
npm run build
HOST=0.0.0.0 PORT=3000 node build/index.js