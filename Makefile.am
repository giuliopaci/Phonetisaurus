AUTOMAKE_OPTIONS = subdir-objects
ACLOCAL_AMFLAGS = -I .autoconf/m4

EXTRA_DIST=               	                       			  \
	$(srcdir)/LICENSE						  \
	$(srcdir)/README.md						  \
	$(srcdir)/docs/doxygen.cfg					  \
	$(srcdir)/docs/mainpage.dox					  \
	$(srcdir)/src/3rdparty/rnnlm/COPYRIGHT.txt			  \
	$(srcdir)/src/3rdparty/utfcpp/utf8/checked.h			  \
	$(srcdir)/src/3rdparty/utfcpp/utf8/core.h			  \
	$(srcdir)/src/3rdparty/utfcpp/utf8/unchecked.h			  \
	$(srcdir)/src/3rdparty/utfcpp/utf8.h				  \
	$(srcdir)/src/lib/feature-reader.cc				  \
	$(srcdir)/src/include/RnnLMPy.h					  \
	$(srcdir)/python/phonetisaurus-module.py			  \
	$(srcdir)/python/script/phoneticize.py				  \
	$(srcdir)/python/script/demo.html				  \
	$(srcdir)/python/script/words.list				  \
	$(srcdir)/python/script/g2pserver.py				  \
	$(srcdir)/python/phonetisaurus/__init__.py			  \
	$(srcdir)/python/pybindgen/__init__.py				  \
	$(srcdir)/python/pybindgen/cppclass_typehandlers.py		  \
	$(srcdir)/python/pybindgen/cppexception.py			  \
	$(srcdir)/python/pybindgen/cppmethod.py				  \
	$(srcdir)/python/pybindgen/enum.py				  \
	$(srcdir)/python/pybindgen/wscript				  \
	$(srcdir)/python/pybindgen/cppclass.py				  \
	$(srcdir)/python/pybindgen/cppclass_container.py		  \
	$(srcdir)/python/pybindgen/settings.py				  \
	$(srcdir)/python/pybindgen/function.py				  \
	$(srcdir)/python/pybindgen/utils.py				  \
	$(srcdir)/python/pybindgen/module.py				  \
	$(srcdir)/python/pybindgen/typehandlers/__init__.py		  \
	$(srcdir)/python/pybindgen/typehandlers/codesink.py		  \
	$(srcdir)/python/pybindgen/typehandlers/ctypeparser/__init__.py	  \
	$(srcdir)/python/pybindgen/typehandlers/ctypeparser/tokenizer.py  \
	$(srcdir)/python/pybindgen/typehandlers/stringtype.py		  \
	$(srcdir)/python/pybindgen/typehandlers/pyobjecttype.py		  \
	$(srcdir)/python/pybindgen/typehandlers/inttype.py		  \
	$(srcdir)/python/pybindgen/typehandlers/doubletype.py		  \
	$(srcdir)/python/pybindgen/typehandlers/voidtype.py		  \
	$(srcdir)/python/pybindgen/typehandlers/floattype.py		  \
	$(srcdir)/python/pybindgen/typehandlers/base.py			  \
	$(srcdir)/python/pybindgen/typehandlers/booltype.py		  \
	$(srcdir)/python/pybindgen/cppattribute.py			  \
	$(srcdir)/python/pybindgen/gccxmlparser.py			  \
	$(srcdir)/python/pybindgen/overloading.py			  \
	$(srcdir)/python/pybindgen/pytypeobject.py			  \
	$(srcdir)/python/pybindgen/container.py				  \
	$(srcdir)/python/pybindgen/converter_functions.py		  \
	$(srcdir)/python/pybindgen/version.py				  \
	$(srcdir)/python/pybindgen/wrapper_registry.py			  \
	$(srcdir)/python/setup.py


dist_bin_SCRIPTS =                     \
	src/bin/phonetisaurus-apply    \
	src/bin/phonetisaurus-train

bin_PROGRAMS =                     \
	phonetisaurus-align	   \
	phonetisaurus-arpa2wfst	   \
	phonetisaurus-g2pfst       \
	phonetisaurus-g2prnn       \
	rnnlm

AM_CPPFLAGS = -I$(top_srcdir)/src -DGIT_REVISION=\"$(GIT_REVISION)\" -std=c++0x -Wall -Wno-sign-compare -Wno-unused-local-typedefs

phonetisaurus_align_SOURCES = src/bin/phonetisaurus-align.cc src/include/PhonetisaurusRex.h src/lib/util.cc src/include/util.h src/lib/LatticePruner.cc src/include/LatticePruner.h src/lib/M2MFstAligner.cc src/include/M2MFstAligner.h
phonetisaurus_align_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/src/3rdparty/utfcpp
phonetisaurus_align_LDADD = $(OPENFST_LDFLAGS)

phonetisaurus_arpa2wfst_SOURCES = src/bin/phonetisaurus-arpa2wfst.cc src/include/ARPA2WFST.h src/lib/util.cc src/include/util.h
phonetisaurus_arpa2wfst_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/src/3rdparty/utfcpp
phonetisaurus_arpa2wfst_LDADD = $(OPENFST_LDFLAGS)

phonetisaurus_g2pfst_SOURCES = src/bin/phonetisaurus-g2pfst.cc src/include/PhonetisaurusScript.h src/include/PhonetisaurusRex.h src/lib/util.cc src/include/util.h
phonetisaurus_g2pfst_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/src/3rdparty/utfcpp -funroll-loops -ffast-math
phonetisaurus_g2pfst_LDADD = $(OPENFST_LDFLAGS)

phonetisaurus_g2prnn_SOURCES = src/bin/phonetisaurus-g2prnn.cc src/include/LegacyRnnLMHash.h src/include/LegacyRnnLMDecodable.h src/include/LegacyRnnLMReader.h src/include/RnnLMDecoder.h src/lib/util.cc src/include/util.h src/3rdparty/rnnlm/rnnlmlib.cpp src/3rdparty/rnnlm/rnnlmlib.h
phonetisaurus_g2prnn_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/src/3rdparty/utfcpp -I$(top_srcdir)/src/3rdparty/rnnlm -funroll-loops -ffast-math
phonetisaurus_g2prnn_LDADD = $(OPENFST_LDFLAGS)
if OPENMP
  phonetisaurus_g2prnn_CXXFLAGS += $(OPENMP_CXXFLAGS)
  phonetisaurus_g2prnn_LDADD += $(OPENMP_LDFLAGS)
endif

rnnlm_SOURCES = src/bin/rnnlm.cc src/3rdparty/rnnlm/rnnlmlib.cpp src/3rdparty/rnnlm/rnnlmlib.h
rnnlm_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/src/3rdparty/rnnlm -funroll-loops -ffast-math
rnnlm_LDADD = $(OPENFST_LDFLAGS)

if HAVE_PYTHON

Phonetisaurus-binding.cc: python/phonetisaurus-module.py
	$(PYTHON) -B $(top_srcdir)/python/phonetisaurus-module.py > Phonetisaurus-binding.cc

CLEANFILES = Phonetisaurus-binding.cc

if HAVE_PYTHON_DEV
pyexec_LTLIBRARIES = Phonetisaurus.la
nodist_Phonetisaurus_la_SOURCES = Phonetisaurus-binding.cc src/lib/util.cc src/include/util.h
Phonetisaurus_la_CXXFLAGS = $(OPENFST_CXXFLAGS) $(PYTHON_CPPFLAGS) -I$(top_srcdir)/src/3rdparty/utfcpp -funroll-loops -ffast-math
Phonetisaurus_la_LIBADD = $(OPENFST_LDFLAGS) $(PYTHON_LIBS)
Phonetisaurus_la_LDFLAGS = -avoid-version -module
endif
endif

all-local:
	cd "$(srcdir)"/python; $(PYTHON) setup.py build --build-base $(abs_builddir)/python/build --verbose

install-exec-local:
	$(PYTHON) "$(srcdir)"/python/setup.py install --prefix "$(DESTDIR)$(prefix)" --single-version-externally-managed --record "$(DESTDIR)$(pkgpythondir)"install_files.txt --verbose

uninstall-local:
	"$(DESTDIR)$(pkgpythondir)"install_files.txt | xargs rm -f
