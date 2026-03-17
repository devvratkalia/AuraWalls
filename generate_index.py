import os
import json

# REPLACE 'yourusername' and 'YourRepoName' with your actual GitHub details
BASE_URL = "https://raw.githubusercontent.com/devvratkalia/AuraWalls/main/"
data = {"categories": []}

# Scan the root directory
for item in sorted(os.listdir('.')):
    # Look only for valid category folders (ignore hidden .git folders or files)
    if os.path.isdir(item) and not item.startswith('.'):
        category = {"name": item, "images": []}
        
        # Scan inside the category folder for images
        for file in sorted(os.listdir(item)):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Create the direct raw download link
                image_url = f"{BASE_URL}{item}/{file}"
                category["images"].append(image_url)
        
        # Only add the category if it actually has images inside
        if category["images"]:
            category["coverImage"] = category["images"][0] # Use the first image as the block cover
            data["categories"].append(category)

# Save the map to index.json
with open('index.json', 'w') as f:
    json.dump(data, f, indent=2)
    
print("Successfully generated index.json!")
