# Use official Node.js image
FROM node:18

# Set working directory inside the container
WORKDIR /app

# Add build argument for API URL
ARG REACT_APP_API_URL=http://localhost:8000

# Copy frontend files
COPY . /app

# Install dependencies
RUN npm install

# Build the React app
RUN npm run build

# Use Nginx to serve the React build
FROM nginx:alpine

# Copy the built React app to Nginx
COPY --from=0 /app/build /usr/share/nginx/html

# Expose frontend port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
