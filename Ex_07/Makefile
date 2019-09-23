# Check OS
ifeq ($(OS),Windows_NT)
UNAME:=windows32
PTHN=python
else
UNAME:=(shell uname)
PTHN=python3
endif

ifeq ($(UNAME),windows32)
ARG_01=ARGUMENT_01
else
ARG_01=ARGUMENT_01
endif

SRC_FILE=ex_07.py

all:
	@$(PTHN) $(SRC_FILE) $(ARG_01)

clean:
	@echo clean ...
	@pause

run:
	@echo command line : $(PTHN) $(SRC_FILE) $(ARG_01)
	$(PTHN) $(SRC_FILE) $(ARG_01)
	pause
