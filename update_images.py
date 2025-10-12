#!/usr/bin/env python3
"""
Helper script to download images from BAPS website and update the portfolio
"""

import os
import requests
from pathlib import Path

# Configuration
IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)

def download_image(url, filename):
    """Download an image from URL and save it locally"""
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        filepath = IMAGES_DIR / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"✓ Saved to {filepath}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def update_html_with_images(profile_img, gallery_images):
    """Update index.html with actual image paths"""
    html_path = Path("index.html")
    
    with open(html_path, 'r') as f:
        content = f.read()
    
    # Update profile image
    profile_placeholder = '''<div class="image-placeholder">
                    <p>Your Photo</p>
                </div>'''
    
    profile_replacement = f'''<img src="images/{profile_img}" alt="Param Patel" 
                     style="width: 300px; height: 300px; border-radius: 50%; 
                            object-fit: cover; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);">'''
    
    content = content.replace(profile_placeholder, profile_replacement)
    
    # Update gallery images
    for i, img_file in enumerate(gallery_images, 1):
        gallery_placeholder = f'''<div class="gallery-placeholder">
                    <p>Event Photo {i}</p>
                </div>'''
        
        gallery_replacement = f'''<img src="images/{img_file}" alt="KDC 2024 Event" 
         style="width: 100%; height: 250px; object-fit: cover;">'''
        
        content = content.replace(gallery_placeholder, gallery_replacement)
    
    # Write updated content
    with open(html_path, 'w') as f:
        f.write(content)
    
    print(f"\n✓ Updated {html_path} with image paths")

def main():
    print("=" * 60)
    print("ePortfolio Image Updater")
    print("=" * 60)
    print()
    
    # Option 1: Download from URLs
    print("Option 1: Download images from URLs")
    print("-" * 60)
    
    # Get profile image
    profile_url = input("Enter URL for your profile photo (or press Enter to skip): ").strip()
    profile_filename = "profile.jpg"
    
    if profile_url:
        download_image(profile_url, profile_filename)
    else:
        print("Skipped profile photo - please add manually to images/ folder")
    
    # Get gallery images
    print("\nNow let's get the KDC event photos...")
    print("Enter image URLs one by one (press Enter without URL when done):\n")
    
    gallery_urls = []
    i = 1
    while True:
        url = input(f"KDC Photo {i} URL (or Enter to finish): ").strip()
        if not url:
            break
        gallery_urls.append(url)
        i += 1
    
    # Download gallery images
    gallery_filenames = []
    for idx, url in enumerate(gallery_urls, 1):
        filename = f"kdc{idx}.jpg"
        if download_image(url, filename):
            gallery_filenames.append(filename)
    
    # Option 2: Use local images
    if not gallery_filenames:
        print("\n" + "=" * 60)
        print("Option 2: Use images already in images/ folder")
        print("-" * 60)
        
        if IMAGES_DIR.exists():
            existing_images = sorted([f.name for f in IMAGES_DIR.glob("*") 
                                     if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']])
            if existing_images:
                print("\nFound these images:")
                for img in existing_images:
                    print(f"  - {img}")
                
                use_existing = input("\nUse these images? (y/n): ").strip().lower()
                if use_existing == 'y':
                    if 'profile.jpg' in existing_images or 'profile.png' in existing_images:
                        profile_filename = 'profile.jpg' if 'profile.jpg' in existing_images else 'profile.png'
                    
                    gallery_filenames = [img for img in existing_images 
                                        if img.startswith('kdc') or img.startswith('event')]
    
    # Update HTML
    if gallery_filenames or profile_filename:
        print("\n" + "=" * 60)
        update_choice = input("\nUpdate HTML with these images? (y/n): ").strip().lower()
        if update_choice == 'y':
            update_html_with_images(profile_filename, gallery_filenames)
            print("\n✓ All done! Open index.html in your browser to preview.")
        else:
            print("Skipped HTML update. You can manually update the image paths.")
    else:
        print("\nNo images to process. Please add images and try again.")
    
    print("\n" + "=" * 60)
    print("Next Steps:")
    print("1. Review your changes in index.html")
    print("2. Test by opening index.html in a web browser")
    print("3. Deploy to GitHub Pages when ready")
    print("=" * 60)

if __name__ == "__main__":
    main()

