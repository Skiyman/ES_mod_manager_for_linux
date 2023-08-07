DESTDIR=

all:
	rm -rf build/esmodmanager
	mkdir -p build/esmodmanager
	cp -r src/* build/esmodmanager
	cp -r esmodmanager.desktop build/esmodmanager

	find build/esmodmanager -type d -name "__pycache__" -exec rm -rf {} +

install:
	rm -rf ${DESTDIR}/opt/esmodmanager
	mkdir -p ${DESTDIR}/opt
	cp -r build/esmodmanager ${DESTDIR}/opt/esmodmanager
	mkdir -p ${DESTDIR}/usr/bin
	mkdir -p ${DESTDIR}/usr/share/applications
	cp src/manager_entrypoint.py ${DESTDIR}/usr/bin/esmodmanager
	cp esmodmanager.desktop ${DESTDIR}/usr/share/applications

