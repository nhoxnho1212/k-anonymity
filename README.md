# k-anonymity

> $K is k anonymity
>
> $DATA_SOURCE is data source path
>
> $RETURN_SOURCE is return data source path

## Run

```shell
python3 main.py
```

## Parameter options

- `-k` : K anonymity
- `-d`: data source path
- `-r`: return data source path

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

## Environment file

You can use parameters in commands or `.env` file

```shell
# .env
K=$K
DATA_SOURCE=$DATA_SOURCE
RETURN_SOURCE=$RETURN_SOURCE
```

## Result

Result csv file will store in `./result/` directory with pattern `adult_$K.csv` or custom parameter.

