# How to Add Images to Your ePortfolio

## Step 1: Download Images from BAPS Detroit Website

1. **Visit the KDC 2024 page:**
   - Go to [baps.org/detroit](https://baps.org/detroit)
   - Look for the Kids Diwali Celebration 2024 event
   - Navigate to the photos/gallery section

2. **Download the images:**
   - Right-click on each image you want to use
   - Select "Save Image As..."
   - Save to your computer with descriptive names like:
     - `kdc1.jpg`
     - `kdc2.jpg`
     - `kdc3.jpg`
     - etc.

3. **Create images folder:**
   ```bash
   cd /Users/parampatel/Downloads/honorsEGL_application
   mkdir images
   ```

4. **Move your downloaded images to the images folder**

## Step 2: Add Your Profile Photo

Save your personal photo as `images/profile.jpg`

## Step 3: Update the HTML

### For Your Profile Photo

**Find this section in `index.html` (around line 65-68):**
```html
<div class="image-placeholder">
    <p>Your Photo</p>
</div>
```

**Replace it with:**
```html
<img src="images/profile.jpg" alt="Param Patel" 
     style="width: 300px; height: 300px; border-radius: 50%; 
            object-fit: cover; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);">
```

### For Gallery Images

**Find the gallery section in `index.html` (around line 370+):**

Each gallery item looks like this:
```html
<div class="gallery-item">
    <div class="gallery-placeholder">
        <p>Event Photo 1</p>
    </div>
    <p class="gallery-caption">Kids Diwali Celebration</p>
</div>
```

**Replace each placeholder with:**
```html
<div class="gallery-item">
    <img src="images/kdc1.jpg" alt="Kids Diwali Celebration" 
         style="width: 100%; height: 250px; object-fit: cover;">
    <p class="gallery-caption">Kids Diwali Celebration</p>
</div>
```

## Step 4: Alternative - Use Image URLs Directly

If the BAPS website allows direct image linking, you can use the image URLs directly:

```html
<img src="https://baps.org/detroit/path-to-image.jpg" alt="KDC 2024">
```

**Note:** This requires the images to be publicly accessible URLs.

## Quick Reference: All Image Locations to Update

1. **Profile Photo** (line ~65):
   - Replace: `<div class="image-placeholder">...</div>`
   - With: `<img src="images/profile.jpg"...>`

2. **Gallery Photos** (lines ~370-410):
   - 6 gallery placeholders to replace
   - Update each with corresponding KDC images

## After Adding Images

1. Save all changes to `index.html`
2. Test locally by opening `index.html` in your browser
3. If images show correctly, you're ready to deploy!
4. Push to GitHub with the images folder included

## Need Help?

If you're having trouble:
1. Make sure image file names match exactly (case-sensitive!)
2. Ensure images are in the `images/` folder
3. Check that the file paths in HTML are correct
4. Test in a web browser before deploying

