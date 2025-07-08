# Datei: Dockerfile.tailwind

FROM node:18-alpine

WORKDIR /app

# Install only once if package-lock.json exists
COPY website/theme/static_src/package*.json ./
RUN npm install

# Copy rest of the Tailwind source files
COPY website/theme/static_src/ ./

# Default command to build Tailwind CSS
CMD ["npm", "run", "build"]
