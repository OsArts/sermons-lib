SHELL=./scripts/activate.sh
### ^^ https://stackoverflow.com/questions/50409515/how-to-activate-a-virtualenv-using-a-makefile 

FILE=main
pipe = se cl

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

.PHONY: se
se:
	@python3 ./scripts/get_2022.py

.PHONY: cl
cl:
	@echo Transform data now!
	@python3 ./scripts/cleaner.py

data: $(pipe)
