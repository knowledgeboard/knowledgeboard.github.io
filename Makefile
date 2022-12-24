FILES = movies school ai graphics vim it other

TEMPLATE = templates

PROGRAM = $(TEMPLATE)/setup.py

TEMPLATE_FILE = $(TEMPLATE)/template.html

SOURCES = $(addprefix $(TEMPLATE)/, $(addsuffix .md, $(FILES)))
TARGET = $(addsuffix .html, $(FILES))

build: $(TARGET)
publish: $(TARGET)pub

$(TARGET): $(SOURCES)
	@echo building $(SOURCES)
	python3 $(PROGRAM) $(TEMPLATE_FILE) $(SOURCES)

# $(TARGET)pub: $(SOURCES)
	# $(build)
	# @echo publishing to Github
	# git commit $(TARGET) $(SOURCES) -m "$(date) publish"
