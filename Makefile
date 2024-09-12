SHELL=./scripts/activate.sh
### ^^ https://stackoverflow.com/questions/50409515/how-to-activate-a-virtualenv-using-a-makefile 

FILE=main
pipe = se cl

# https://stackoverflow.com/questions/6273608/how-to-pass-argument-to-makefile-from-command-line

%:
	@:
args = 'arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}'

.PHONY: run
run:
	@npm run dev -- --host 192.168.0.101

.PHONY: bu
bu:
	@npm run build

# .PHONY: act
# act:
# 	# Activated venv
# 	@source ./.venv/bin/activate;
# 	@echo You are ✅ in -VENV- now;
	

# .PHONY: act

# act:
# 	@echo "Activating virtual environment..."
# 	@. ./activate.sh

.PHONY: pa
pa:
	@python3 ./scripts/parse.py

# SERMONS
.PHONY: se
se:
	@python3 ./scripts/get_2022.py

.PHONY: cl
cl:
	@echo Transform data now!
	@python3 ./scripts/cleaner.py

data: $(pipe)

# Create sabbats sys.argv[1]
.PHONY: sb
sb:
	@python3 ./scripts/sabbats.py $(VAR)

test:
	@echo $(call args,defaultstring)

# Предварительная очистка файла(сформированного из копирования со страницы хтм в ЗАМЕТКИ, а потом перенесённых в саблайм-текст)
.PHONY: sp
sp:
	@python3 ./scripts/space_cleaner.py $(DATAFILE)