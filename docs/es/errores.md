# ERRORES

Aqui quiero dejar todos los erroes que he cometidos y como los he ido solucionando.

## ERROES DE MANEJO DE PYTHON

Bueno tenia el siguiente error

```bash
get channel YouTube statistics and information
  0%|                                                                                                                                                   | 0/1 [00:00<?, ?it/s]Could not get channel statistics and information
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.32s/it]
get the videos data of the channel YouTube specified
Error! Could not get correct channel data!
 {'error': {'code': 400, 'message': 'Request contains an invalid argument.', 'errors': [{'message': 'Request contains an invalid argument.', 'domain': 'global', 'reason': 'badRequest'}], 'status': 'INVALID_ARGUMENT'}}
```

Que se producía como si estuviese llamando en python el código del main, pero sucedida que.. como no tengo el api key en otro archivo en congif, cuando lo llamaba del main este se ejecutaba todo lo que estaba en el main, que no estaba en una función si no como scrpipting y Linea a linea y como python ejecuta todo linea a linea, pues esto lo que hacia era ejecutar obviamente lo que estaba ahi, no entendía porque se estaba ejecutando.

Asi estaba el ``main.py``

```python

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

from youtubeAPI.requestsYoutube import YTstats

yt = YTstats(API_KEY, "")
yt.extract_all()
yt.dump_to_json()  # dumps to .json

```

Que cuando llamaba el `API_KEY` desde otro archivo se terminaba ejecutando todo el archivo ``main.py``, de ahi porque se suele separar las cosas del config a otro archivo, pero como por ahora no es necesario tener otro archivo llamado ``config.py``  que solamente va a tener 4 lienas de codigos y menos de 50 palabras, la solución mas sencilla seria encapsularlo y ya "encapsularlo y ya en una función", que haga la principal tarea como en un ``main():`` como se suele hacer en los programas de python.

asi:

```python
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

def main():
    from youtubeAPI.requestsYoutube import YTstats

    ch_id = r'\%40ladomicilio'
    yt = YTstats(api_key=API_KEY, channel_id=ch_id)
    yt.extract_all()
    yt.dump_to_json()  # dumps to .json
    
    return "Se ejecuto el programa, todo salio bien?"
```

## IMPORTACION  de variable y quedar una función en la llamada del script

Tuve un error similar a este esaba en el archivo de ``"Teste.py`` y estaba intentando importar el ``API_KEY`` desde el archivo ``main.py``, pero como dice la teoría de python, si al importar algo de otro archivo se trae todo lo que esta en ese archivo y se ejecuta todo lo que este ahi siempre y cuando se halla llamado, asi funciona el interprete interpreta todo.

## e IMPORTACION de paquete

de la libreria tqdm solo lo importe como:

```python
import tqdm
```

La manera correcta de importar esta librería es:

```python
from tqdm import tqdm
```

El error que arrojo el Shell y el interprete fue:

```shell
Traceback (most recent call last):
  File ".\src\test.py", line 60, in <module>
    print(test_statisctic_channel())
  File ".\src\test.py", line 50, in test_statisctic_channel
    pbar = tqdm(total=1)
TypeError: 'module' object is not callable
```

Asi que busque en internet lei un articulo de freecodecamp no entendí mucho, estaba en ingles, pero luego vi la pagina oficial de `tqdm` y vi como es la manera correcta de importarlo asi que lo corregí y listo.

## TODO

``~ “ # % & * : < > ? / \ { | }``

Para limpiar el contenido, de los titulos

## COMO OBTENER EL ID DE UN CANAL DE YOUTUBE

bUENO recientemente, esto se hizo dificl, youtube cambiom ciertas cosas que llegaron para quedarse y que de verdad ayudan al usuario y como una red social que es se estaba quedando.