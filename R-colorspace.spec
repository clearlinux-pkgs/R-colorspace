#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-colorspace
Version  : 1.3.2
Release  : 37
URL      : http://cran.r-project.org/src/contrib/colorspace_1.3-2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/colorspace_1.3-2.tar.gz
Summary  : Color Space Manipulation
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-colorspace-lib
BuildRequires : R-dichromat
BuildRequires : R-mvtnorm
BuildRequires : clr-R-helpers
BuildRequires : tcl

%description
RGB, HSV, HLS, CIEXYZ, CIELUV, HCL (polar CIELUV),
	     CIELAB and polar CIELAB. Qualitative, sequential, and
	     diverging color palettes based on HCL colors are provided
	     along with an interactive palette picker (with either a Tcl/Tk
	     or a shiny GUI).

%package lib
Summary: lib components for the R-colorspace package.
Group: Libraries

%description lib
lib components for the R-colorspace package.


%prep
%setup -q -c -n colorspace

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502397766

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502397766
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library colorspace
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library colorspace
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library colorspace
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library colorspace
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/colorspace/CITATION
/usr/lib64/R/library/colorspace/DESCRIPTION
/usr/lib64/R/library/colorspace/INDEX
/usr/lib64/R/library/colorspace/LICENSE
/usr/lib64/R/library/colorspace/Meta/Rd.rds
/usr/lib64/R/library/colorspace/Meta/data.rds
/usr/lib64/R/library/colorspace/Meta/features.rds
/usr/lib64/R/library/colorspace/Meta/hsearch.rds
/usr/lib64/R/library/colorspace/Meta/links.rds
/usr/lib64/R/library/colorspace/Meta/nsInfo.rds
/usr/lib64/R/library/colorspace/Meta/package.rds
/usr/lib64/R/library/colorspace/Meta/vignette.rds
/usr/lib64/R/library/colorspace/NAMESPACE
/usr/lib64/R/library/colorspace/NEWS
/usr/lib64/R/library/colorspace/R/colorspace
/usr/lib64/R/library/colorspace/R/colorspace.rdb
/usr/lib64/R/library/colorspace/R/colorspace.rdx
/usr/lib64/R/library/colorspace/data/Rdata.rdb
/usr/lib64/R/library/colorspace/data/Rdata.rds
/usr/lib64/R/library/colorspace/data/Rdata.rdx
/usr/lib64/R/library/colorspace/doc/hcl-colors.R
/usr/lib64/R/library/colorspace/doc/hcl-colors.Rnw
/usr/lib64/R/library/colorspace/doc/hcl-colors.pdf
/usr/lib64/R/library/colorspace/doc/index.html
/usr/lib64/R/library/colorspace/hclwizard/html/GrADS.html
/usr/lib64/R/library/colorspace/hclwizard/html/help.html
/usr/lib64/R/library/colorspace/hclwizard/html/matlab.html
/usr/lib64/R/library/colorspace/hclwizard/html/python.html
/usr/lib64/R/library/colorspace/hclwizard/prepareStaticContent.R
/usr/lib64/R/library/colorspace/hclwizard/server.R
/usr/lib64/R/library/colorspace/hclwizard/ui.R
/usr/lib64/R/library/colorspace/hclwizard/www/hclwizard.css
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_alt_heat.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_alt_terrain.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-red.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-red_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-red_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blues.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blues_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_bpy.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_brbg.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_bupu.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_cm.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_cold.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_dark_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_dynamic.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_even_darker.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_green-orange.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_greens.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_greys.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_harmonic.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_heat.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_heat_hcl.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_light_grays.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_oranges.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_pastel_1.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_piyg.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_plasma.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_prgn.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_puor.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_pure_red.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purples.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_rainbow.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_rdbu.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_red_blue.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_reds.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_set_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_set_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_terrain.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_terrain_hcl.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_topo.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_viridis.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_warm.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_yellow-blue.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_yellow-green.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_yellow-red.png
/usr/lib64/R/library/colorspace/help/AnIndex
/usr/lib64/R/library/colorspace/help/aliases.rds
/usr/lib64/R/library/colorspace/help/colorspace.rdb
/usr/lib64/R/library/colorspace/help/colorspace.rdx
/usr/lib64/R/library/colorspace/help/paths.rds
/usr/lib64/R/library/colorspace/html/00Index.html
/usr/lib64/R/library/colorspace/html/R.css
/usr/lib64/R/library/colorspace/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/colorspace/libs/colorspace.so
/usr/lib64/R/library/colorspace/libs/colorspace.so.avx2
/usr/lib64/R/library/colorspace/libs/colorspace.so.avx512
