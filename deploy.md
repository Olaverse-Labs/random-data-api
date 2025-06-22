# Deploy to Elest.io

This guide will help you deploy your Random Data Generator API to Elest.io.

## Prerequisites

1. **Elest.io Account**: Sign up at [elest.io](https://elest.io)
2. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, etc.)
3. **Docker Knowledge**: Basic understanding of Docker (optional, but helpful)

## Deployment Steps

### 1. Prepare Your Repository

Make sure your repository contains these files:
- `main.py` - Your FastAPI application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration
- `.dockerignore` - Docker ignore rules
- `elestio.yml` - Elest.io configuration

### 2. Connect Your Repository

1. Log in to your Elest.io dashboard
2. Click "New App" or "Deploy"
3. Choose "Deploy from Git"
4. Connect your Git provider (GitHub, GitLab, etc.)
5. Select your repository

### 3. Configure Your App

1. **App Name**: `random-data-generator-api` (or your preferred name)
2. **Branch**: `main` (or your default branch)
3. **Build Command**: Leave empty (uses Dockerfile)
4. **Start Command**: Leave empty (uses Dockerfile CMD)

### 4. Environment Variables

Add these environment variables in the Elest.io dashboard:
```
PYTHONUNBUFFERED=1
PORT=8000
```

### 5. Resources

Recommended settings:
- **CPU**: 0.5 cores
- **Memory**: 512 MB
- **Storage**: 1 GB

### 6. Deploy

1. Click "Deploy"
2. Wait for the build to complete (usually 2-5 minutes)
3. Your app will be available at the provided URL

## Alternative: Using elestio.yml

If you prefer to use the `elestio.yml` configuration file:

1. Make sure `elestio.yml` is in your repository root
2. Elest.io will automatically detect and use this configuration
3. Deploy as normal

## Post-Deployment

### 1. Test Your API

Once deployed, test your endpoints:

```bash
# Test the root endpoint
curl https://your-app-name.elestio.app/

# Test person generation
curl https://your-app-name.elestio.app/api/person

# Test health check
curl https://your-app-name.elestio.app/api/health
```

### 2. Access Documentation

- **Swagger UI**: `https://your-app-name.elestio.app/docs`
- **ReDoc**: `https://your-app-name.elestio.app/redoc`

### 3. Monitor Your App

- Check the logs in the Elest.io dashboard
- Monitor resource usage
- Set up alerts if needed

## Custom Domain (Optional)

1. Go to your app settings in Elest.io
2. Add your custom domain
3. Update your DNS records as instructed
4. Wait for DNS propagation

## Scaling

### Auto-scaling
Your app is configured to scale from 1 to 3 instances based on load.

### Manual scaling
You can adjust the scaling settings in the Elest.io dashboard:
- Go to your app settings
- Modify the scaling configuration
- Apply changes

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check the build logs in Elest.io dashboard
   - Ensure all dependencies are in `requirements.txt`
   - Verify Dockerfile syntax

2. **App Won't Start**
   - Check the application logs
   - Verify the port configuration (should be 8000)
   - Ensure the health check endpoint works

3. **High Resource Usage**
   - Monitor CPU and memory usage
   - Consider upgrading resources
   - Optimize your application if needed

### Logs

Access logs in the Elest.io dashboard:
1. Go to your app
2. Click "Logs"
3. View real-time or historical logs

### Health Checks

Your app includes a health check endpoint at `/api/health`. Elest.io will use this to monitor your app's status.

## Cost Optimization

- Start with minimal resources (0.5 CPU, 512MB RAM)
- Monitor usage and scale up as needed
- Use auto-scaling to handle traffic spikes
- Consider using Elest.io's free tier for testing

## Security

- Your app runs in a secure container
- No root access by default
- HTTPS enabled automatically
- Regular security updates

## Support

If you encounter issues:
1. Check the Elest.io documentation
2. Review your application logs
3. Contact Elest.io support
4. Check the FastAPI documentation

## Example Deployment URL

After successful deployment, your API will be available at:
```
https://random-data-api.elestio.app
```

You can then use it like:
```bash
curl https://random-data-api.elestio.app/api/person
curl https://random-data-api.elestio.app/api/company
curl "https://random-data-api.elestio.app/api/custom?data_type=email&count=5"
``` 