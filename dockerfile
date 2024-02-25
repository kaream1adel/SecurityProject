# Use an official Node.js runtime as a base image
FROM node:latest

# Set the working directory inside the container
WORKDIR /Graduation project/Frontend-Module-main/First version/.

#  Copy package.json and package-lock.json to leverage Docker cache
COPY package*.json ./

# Clear npm cache and install app dependencies
RUN npm cache clean --force && npm install

# Update npm to the latest version
RUN npm install -g npm@latest

RUN  npm install express

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on
#EXPOSE 3000

# Define the command to run your application
CMD ["node", "server.js"]