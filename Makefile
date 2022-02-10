
clean:
	ls
	pwd
	- rm contracts/*
	- rm -rf *egg-infp*
	- rm -rf .idea

build:
	make clean
	- python3 nftizer/build_contract.py