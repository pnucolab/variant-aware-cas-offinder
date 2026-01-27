FROM node:22-alpine
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

RUN mkdir /app
WORKDIR /app

COPY package.json .
RUN pnpm install

COPY . .

EXPOSE 3000

ENTRYPOINT ["/bin/sh", "./start.sh"]