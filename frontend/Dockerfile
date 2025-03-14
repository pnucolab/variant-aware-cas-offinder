FROM node:19-alpine
RUN mkdir /app
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
EXPOSE 3000

CMD ["node", "build/index.js"]