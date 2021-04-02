FROM node:9-slim
WORKDIR /app
COPY package.json /app

RUN npm install
RUN npm install @tensorflow/tfjs @tensorflow-models/handpose react-webcam
COPY . /app
EXPOSE 8080
ENTRYPOINT HOST="0.0.0.0" npm start app.js 
