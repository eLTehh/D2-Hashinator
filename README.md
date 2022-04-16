# D2-Hashinator
Maps hashes to image names for dumped PPSSPP textures of Tales of Destiny 2.
Requires: 
- inputTex folder (Input the original image you want to compare + rename it to the replaced texture name)
- dumpedTex folder (The dumped textures from D2, which I will not be providing)

Could be optimized some more with a binary search for image size (width, height), I feel. 
Haven't implemented since my samples run in ~1s which isn't too bad if I'm mapping hashes once every version update.

Hard coded for D2 skit faces specifically (see cropcoords variable), mostly to eliminate noise. Could be modified to match hashes for other games.
