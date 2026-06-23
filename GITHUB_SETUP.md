# Setup Instructions for GitHub

Follow these steps to push your SSH Portfolio to GitHub:

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Enter repository name: `ssh-portfolio`
3. Choose visibility: **Public** (for portfolio)
4. Click **Create repository**

## Step 2: Add Remote and Push

Copy and paste the commands below in your terminal (replace `YOUR_USERNAME` with your GitHub username):

```bash
cd /home/madan/ssh-portfolio

# Add GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/ssh-portfolio.git

# Rename main branch if needed (GitHub default is 'main')
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 3: Verify

Visit: https://github.com/YOUR_USERNAME/ssh-portfolio

You should see all 36 files with commit history!

## Using SSH Keys (Optional but Recommended)

If you have SSH keys configured:

```bash
git remote set-url origin git@github.com:YOUR_USERNAME/ssh-portfolio.git
git push -u origin main
```

## Troubleshooting

### Push rejected: Repository already exists
```bash
git remote remove origin
# Then repeat Step 2
```

### Authentication failed
- Use Personal Access Token: https://github.com/settings/tokens
- Select `repo` scope
- Paste token when prompted for password

### Permission denied (publickey)
- Ensure SSH keys are added to GitHub: https://github.com/settings/ssh/new
- Or use HTTPS instead of SSH
