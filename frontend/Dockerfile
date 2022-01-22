# syntax=docker/dockerfile:1
FROM node:17.4.0-alpine
WORKDIR /frontend
COPY package.json /frontend/
RUN npm install
COPY . /frontend/
