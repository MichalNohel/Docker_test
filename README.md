# docker_simple_example

# vytvoření image na dockerhubu:
## ve wsl:
```
cd /home/nohel/Docker_test

docker build -t muj_image .
```

## otestovat interaktivne
```
docker run --rm -it --gpus all --name muj_kontejner -v ./example_data:/workspace/example_data muj_image bash

python example_code.py example_data/data.txt 

exit


## pushnout 

```
docker login -u tomasvicar
docker tag muj_image tomasvicar/muj_image:latest
docker push tomasvicar/muj_image:latest
```
> latest nebo jakékoliv jiné pojmenování verze (1.0.0 ...)

# use it:
```
docker run --rm -it --gpus all --name muj_kontejner2 -v .:/workspace tomasvicar/muj_image:latest bash
python example_code.py example_data/data.txt 
exit
```
> --rm kontejner po použití smaze; --gpus all povolí gpu;  

# nebo jedním rádkem
```
docker run --rm  --gpus all --name muj_stazeny -v ./Docker_test/example_data:/workspace/data nohelm/muj_image:latest python example_code.py data/data.txt
```
> jen spustí kod a po doběhnutí zavře (narozdíl od přechozího co otevřelo terminal v dockeru)

docker run --rm  --gpus all --name muj_stazeny -v ./tmp_data:/workspace/data nohelm/muj_image:latest python example_code.py data/data.txt