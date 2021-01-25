# k-anonymity

> ``` $K``` is k anonymity

## Run

```shell
python3 main.py -k $K
```

## Run with Docker via "ano" CLI support

- Build container

    ```shell
    ./ano build
    ```

- Run container

    ```shell
    ./ano run
    ```

By default $K = 2

You can use parameter k in commands or `.env` file

```shell
./ano run -k $K
```

```shell
# .env
K=$K
```

## Result

Result csv file will store in `./result/` directory with pattern `adult_$K.csv`.

