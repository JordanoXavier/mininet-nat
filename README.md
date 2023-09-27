Como rodar:

    - executar a topologia no mininet
    python3 topo2-nat.py
    

    - abrir o terminal do router e executar nele a função nat
    r xterm &
        - terminal do roteador:
        python3 nat.py


    - abrir o terminal do host1 e executar os testes
    h1 xterm &
        - terminal do host1:
        iperf -c 8.8.8.8 -p 8888 
        iperf -c 8.8.4.4 -p 8844 -u


    - abrir o terminal do host2 e executar os testes
    h2 xterm &
        - terminal do host2:
        iperf -c 8.8.8.8 -p 8888
        iperf -c 8.8.4.4 -p 8844 -u
