# Complete Deployment Guide 🚀

This guide will walk you through getting your ePortfolio live on the internet using GitHub Pages.

## 📋 Pre-Deployment Checklist

Before deploying, make sure you have:

- [ ] Your profile photo
- [ ] KDC event photos from baps.org/detroit
- [ ] All images added to the `images/` folder
- [ ] Updated `index.html` with your images
- [ ] Tested the site locally in a browser

## 🖼️ Step 1: Get Your Images

### Getting KDC Photos from BAPS Detroit Website

1. Go to **https://baps.org/detroit**
2. Look for the "Events" or "Gallery" section
3. Find "Kids Diwali Celebration 2024" or "KDC 2024"
4. Right-click on each photo you want to use
5. Select "Save Image As..." 
6. Save with names like: `kdc1.jpg`, `kdc2.jpg`, etc.

**Tip:** Choose 6-8 high-quality photos that show:
- The venue/decorations
- Kids enjoying the celebration
- Stage performances
- Community gathering
- Your leadership in action (if available)

### Organizing Your Images

1. Create the images folder:
   ```bash
   cd /Users/parampatel/Downloads/honorsEGL_application
   mkdir images
   ```

2. Move all downloaded images to the `images/` folder:
   - `profile.jpg` - Your photo
   - `kdc1.jpg` through `kdc6.jpg` - Event photos

## 🔧 Step 2: Update the HTML

### Method A: Use the Python Script (Easiest)

```bash
cd /Users/parampatel/Downloads/honorsEGL_application
python3 update_images.py
```

Follow the prompts to update your images automatically.

### Method B: Manual Update

Open `index.html` in a text editor and make these changes:

#### Update Profile Photo (around line 65)

**Find:**
```html
<div class="image-placeholder">
    <p>Your Photo</p>
</div>
```

**Replace with:**
```html
<img src="images/profile.jpg" alt="Param Patel" 
     style="width: 300px; height: 300px; border-radius: 50%; 
            object-fit: cover; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);">
```

#### Update Gallery Photos (around line 370+)

**Find each:**
```html
<div class="gallery-placeholder">
    <p>Event Photo 1</p>
</div>
```

**Replace with:**
```html
<img src="images/kdc1.jpg" alt="KDC 2024" 
     style="width: 100%; height: 250px; object-fit: cover;">
```

Repeat for all 6 gallery items, changing `kdc1.jpg` to `kdc2.jpg`, `kdc3.jpg`, etc.

## ✅ Step 3: Test Locally

1. Open `index.html` in your web browser
2. Check that:
   - Your profile photo appears
   - All gallery images load
   - Navigation works smoothly
   - Everything looks good on mobile (resize your browser)

## 🌐 Step 4: Deploy to GitHub Pages

### Create a GitHub Account (if you don't have one)

1. Go to **https://github.com**
2. Click "Sign up"
3. Follow the registration process

### Create Your Repository

1. Once logged in, click the **"+"** icon in the top right
2. Select **"New repository"**
3. **IMPORTANT:** Name it exactly: `YOUR_USERNAME.github.io`
   - Replace `YOUR_USERNAME` with your actual GitHub username
   - Example: if your username is `parampatel123`, name it `parampatel123.github.io`
4. Make it **Public**
5. Do NOT initialize with README, .gitignore, or license
6. Click **"Create repository"**

### Upload Your Files

#### Option A: Using GitHub Website (Easier for beginners)

1. On your new repository page, click **"uploading an existing file"**
2. Drag and drop ALL these files:
   - `index.html`
   - `styles.css`
   - `script.js`
   - `README.md`
   - The entire `images/` folder (with all your photos)
3. Scroll down and click **"Commit changes"**
4. Wait for the upload to complete

#### Option B: Using Git Command Line

```bash
cd /Users/parampatel/Downloads/honorsEGL_application

# Initialize git repository
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit: ePortfolio for UMich application"

# Set the main branch
git branch -M main

# Connect to GitHub (replace YOUR_USERNAME with your actual username)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.github.io.git

# Push to GitHub
git push -u origin main
```

### Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** (top menu)
3. Click **"Pages"** in the left sidebar
4. Under **"Source"**, select:
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **"Save"**
6. Wait 2-5 minutes for deployment

### Access Your Live Site

Your portfolio will be live at: `https://YOUR_USERNAME.github.io`

## 🎉 Step 5: Share Your Portfolio

Once live, you can share the link in your University of Michigan application!

**Your ePortfolio URL:** `https://YOUR_USERNAME.github.io`

## 🔄 Making Updates Later

If you need to make changes:

1. Edit your files locally
2. Either:
   - **Re-upload** through GitHub website, or
   - **Push changes** using git:
     ```bash
     git add .
     git commit -m "Update content"
     git push
     ```
3. Changes will appear live in 1-2 minutes

## 🆘 Troubleshooting

### Images Not Showing
- Check file names are exact (case-sensitive!)
- Ensure images are in `images/` folder
- Verify paths in HTML: `images/filename.jpg`
- Clear browser cache and refresh

### Site Not Loading
- Wait 5-10 minutes after first deployment
- Check repository name is exactly `username.github.io`
- Ensure GitHub Pages is enabled in Settings > Pages
- Verify `index.html` is in the root directory

### GitHub Pages Not Working
- Make sure repository is Public, not Private
- Check that you selected the correct branch (main)
- Look for error messages in Settings > Pages

### Profile Photo Looks Stretched
- Use a square image (1:1 aspect ratio)
- Recommended size: at least 500x500 pixels
- The CSS will automatically crop it to a circle

## 📱 Testing Checklist

Before submitting, test your site:

- [ ] Works on Chrome
- [ ] Works on Safari/Firefox
- [ ] Works on mobile (iPhone/Android)
- [ ] All images load properly
- [ ] Navigation links work
- [ ] Smooth scrolling works
- [ ] Text is readable
- [ ] No spelling errors

## 🎯 Final Steps for Your Application

1. Copy your live URL: `https://YOUR_USERNAME.github.io`
2. Paste it into your University of Michigan application
3. Take a screenshot as backup
4. Test the link one more time before submitting

---

## 🏆 Success!

Your ePortfolio is now live and ready to impress the University of Michigan admissions committee!

**Go Blue! 〽️**

---

## 📞 Need Help?

If you run into issues:
1. Double-check each step in this guide
2. Search GitHub's help documentation
3. Verify all file names and paths are correct
4. Make sure your repository is public

Good luck with your application! 🎓

