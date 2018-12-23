
SPEC_FILE = gitbucket.spec
DIST = .el7

all:
	$(eval CWD=$(shell pwd))
	$(eval RPM_ROOT=$(CWD)/build/rpm)
	$(eval SOURCE_DIR=$(RPM_ROOT)/SOURCES)

	mkdir -p $(SOURCE_DIR)
	
	git archive HEAD | tar xf - -C $(SOURCE_DIR)
	rpmbuild -ba $(SPEC_FILE) --define "dist $(DIST)" --define "_topdir $(RPM_ROOT)" 

clean:
	rm build -rf
