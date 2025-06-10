docker run --rm \
  --network="host" \
  -v $PWD:/zap/wrk \
  -t zaproxy/zap-stable zap-full-scan.py -t http://127.0.0.1:5000/ -J vulnerableapp.json -I

