import openslide
from openslide.deepzoom import DeepZoomGenerator
x = "AFB 5081A.svs"
raw = openslide.OpenSlide(x)
print(raw)
zslide = DeepZoomGenerator(raw, tile_size=254, overlap=1, limit_bounds=True)    #create_DeepZooom_from_openslide_object,limit_bounds means not include space
level = zslide.level_count      #select_the_level_of_donwzoom default=max
col,row = zslide.level_tiles[level-1]   #get_No._of_col_&_row_tiles 
print("{}\nlevel: {}\ncol: {}\nrow: {}".format(zslide,level,col,row))
n=1
for y in range(row-1):
    for x in range(col-1):
        result = zslide.get_tile(level-1,(x,y))     
        coor,lv,size = zslide.get_tile_coordinates(level-1,(x,y))
        #print(n,result)
        #result.save("({},{})".format(x,y),format='tiff')    #save_PIL_object_to_CWD
        print("{}\tcoordinate = {}\tlevel={}\tsize={}".format(n, coor, lv, size),end='\t\t')
        print("save to\t({},{}).tiff".format(x, y))
        n += 1
raw.close()
