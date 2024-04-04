# Use an official Nginx runtime as the base image
FROM nginx:latest

# Set the working directory in the container
WORKDIR /app

# Copy the Nginx configuration file from the current directory to the container
RUN rm /etc/nginx/conf.d/*.conf
COPY nginx.conf /etc/nginx/nginx.conf


# Expose ports
EXPOSE 80

# Start Nginx and uWSGI when the container launches
CMD ["nginx", "-g", "daemon off;"]
