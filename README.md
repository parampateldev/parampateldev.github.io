# Param Patel - ePortfolio

A modern, responsive ePortfolio showcasing community leadership experience for University of Michigan Honors Program application.

## 🌟 Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Smooth Animations**: Engaging scroll animations and transitions
- **Modern UI**: Clean, professional design with gradient accents
- **Easy to Customize**: Simple HTML structure with organized CSS

## 📁 Project Structure

```
honorsEGL_application/
├── index.html       # Main HTML file
├── styles.css       # All styling
├── script.js        # JavaScript for interactions
├── images/          # Folder for your photos (create this)
└── README.md        # This file
```

## 🚀 Deployment to GitHub Pages

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Name it: `username.github.io` (replace `username` with your actual GitHub username)
4. Make it Public
5. Click "Create repository"

### Step 2: Upload Your Files

**Option A: Using GitHub Website**
1. Click "uploading an existing file"
2. Drag and drop all files (`index.html`, `styles.css`, `script.js`, `README.md`)
3. Click "Commit changes"

**Option B: Using Git (Terminal)**
```bash
cd /Users/parampatel/Downloads/honorsEGL_application
git init
git add .
git commit -m "Initial commit: ePortfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.github.io.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings"
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select "main" branch
5. Click "Save"
6. Your site will be live at: `https://YOUR_USERNAME.github.io`

## 📸 Adding Your Photos

### Step 1: Create an Images Folder
```bash
mkdir images
```

### Step 2: Add Your Photos
Place your photos in the `images/` folder with descriptive names:
- `profile.jpg` - Your photo for About Me
- `kdc1.jpg`, `kdc2.jpg`, etc. - Event photos

### Step 3: Update Image Placeholders in HTML

Replace the placeholder sections in `index.html`:

**For your profile photo (line ~65):**
```html
<!-- Change this: -->
<div class="image-placeholder">
    <p>Your Photo</p>
</div>

<!-- To this: -->
<img src="images/profile.jpg" alt="Param Patel" style="width: 300px; height: 300px; border-radius: 50%; object-fit: cover; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);">
```

**For gallery photos (around line ~370):**
```html
<!-- Change this: -->
<div class="gallery-placeholder">
    <p>Event Photo 1</p>
</div>

<!-- To this: -->
<img src="images/kdc1.jpg" alt="Kids Diwali Celebration" style="width: 100%; height: 250px; object-fit: cover;">
```

## 🎨 Customization Tips

### Change Colors
Edit the CSS variables in `styles.css` (lines 12-20):
```css
:root {
    --primary-color: #2563eb;      /* Main blue color */
    --accent-color: #f59e0b;       /* Orange accent */
    --success-color: #10b981;      /* Green for success cards */
}
```

### Update Content
All text content is in `index.html`. Simply edit the text between HTML tags.

### Add More Photos
Duplicate a gallery item in `index.html` and update the image source and caption.

## 📱 Testing Locally

Simply open `index.html` in your web browser. Double-click the file or right-click and select "Open with" your preferred browser.

## ✅ Checklist Before Submission

- [ ] Add your profile photo
- [ ] Add event photos to gallery
- [ ] Update image placeholders in HTML
- [ ] Test on mobile devices
- [ ] Share the GitHub Pages link
- [ ] Verify all links work

## 🆘 Troubleshooting

**Images not showing?**
- Check file paths are correct
- Ensure images are in the `images/` folder
- Image file names are case-sensitive

**Site not loading on GitHub Pages?**
- Wait 5-10 minutes after pushing changes
- Check that `index.html` is in the root directory
- Verify GitHub Pages is enabled in settings

**Animations not working?**
- Make sure `script.js` is linked in `index.html`
- Check browser console for errors (F12)

## 📞 Need Help?

If you encounter any issues:
1. Check the GitHub Pages documentation
2. Verify all files are uploaded correctly
3. Ensure your repository name is exactly `username.github.io`

## 📄 License

This ePortfolio is created for educational purposes for Param Patel's University of Michigan application.

---

**Good luck with your application! 〽️ Go Blue!**

