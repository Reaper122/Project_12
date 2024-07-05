FROM node:18

WORKDIR /usr/app

COPY package.json .

RUN npm install

RUN npm install axios

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]