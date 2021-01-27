#!/bin/bash

UNAMEOUT="$(uname -s)"


WHITE='\033[1;37m'
NC='\033[0m'


# Verify operating system is supported...
case "${UNAMEOUT}" in 
    Linux*)         MACHINE=linux;;
    Darwin*)        MACHINE=mac;;
    *)              MACHINE="UNKNOWN"
esac

if [ "$MACHINE" == "UNKNOWN" ]; then
    echo "Unsupported operating system [$uname -s]. K-anonynity app supports macOS, Linux."
fi

# Defin environment variables...
export APP_SERVICE=${APP_SERVICE:-"k-anonymity-app"}
export K=${K:-2}
export DATA_SOURCE=${DATA_SOURCE}
export RETURN_SOURCE=${RETURN_SOURCE}

# Ensure that Docker is running...
if ! docker info > /dev/null 2>&1; 
then
    echo -e "${WHITE}Docker is not running.${NC}"

    exit 1

fi




if [ $# -gt 0 ]; then
    # Source the ".env" file
    if [ -f ./.env ]; then
        source ./.env
    fi

    # Proxy Build commands 
    if [ "$1" == "build" ]; then
        shift 1

        docker build -t "$APP_SERVICE" .
    
    # Proxy run commands
    elif [ "$1" == "run" ]; then
        shift 1
        while getopts k:d:r:h: option
        do
            case "${option}"
            in
                k) K=${OPTARG};;
                d) DATA_SOURCE=${OPTARG};;
                r) RETURN_SOURCE=${OPTARG};;
                *)
            esac
        done
        
        docker run --rm -it -e K="$K" -e DATA_SOURCE="$DATA_SOURCE" -e RETURN_SOURCE="$RETURN_SOURCE" -v $(pwd):/k-anonymity "$APP_SERVICE" 
        
    
    # Pass unknown commands
    
    fi

fi

