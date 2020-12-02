# Performance Testing
## How to use
1. use make from current directory as most paths are configures are relative paths.

## Setup env:
Environment can be setup using following commant
```
make init BATCH_SIZE=0
```
### Running tests
Tests can be run using following command
```
make recipe BATCH_SIZE=<int>
```
Here recipes are clipper, tfserve and torch and batch size is [1,2,4,,16,32,64]

so an example is:
```
make clipper BATCH_SIZE=1
```

The results are stored in ```./results``` folder and logs are stored in ```./logs``` folder. The format is ```clipper_${BATCH_SIZE}_${CONDITION}_stats.csv``` etc. and ```clipper_logs_${BATCH_SIZE}_${CONDITION}```