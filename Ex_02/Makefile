PYTN:=python
PRCCR_ARCHCTR:= 
UNAME_S:=

ifeq ($(OS),Windows_NT)
	PYTN=python
	UNAME_S=Windows_NT
	ifeq ($(PROCESSOR_ARCHITECTURE),AMD64)
		PRCCR_ARCHCTR+=AMD64
	endif
	ifeq ($(PROCESSOR_ARCHITECTURE),x86)
		PRCCR_ARCHCTR+=IA32
	endif
else
	UNAME_S=$(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		PYTN:=python3
	endif
	UNAME_P:=$(shell uname -p)
	ifeq ($(UNAME_P), x86_64)
		PRCCR_ARCHCTR+=AMD64
	endif
	ifneq ($(filter %86,$(UNAME_P)),)
		PRCCR_ARCHCTR+=IA32
	endif
	ifneq ($(filter arm%,$(UNAME_P)),)
		PRCCR_ARCHCTR+=ARM
	endif
endif

all:
	@echo $(UNAME_S) $(PRCCR_ARCHCTR)
	$(PYTN) ex_02.py

