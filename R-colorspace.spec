#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-colorspace
Version  : 1.4.0
Release  : 61
URL      : https://cran.r-project.org/src/contrib/colorspace_1.4-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/colorspace_1.4-0.tar.gz
Summary  : A Toolbox for Manipulating and Assessing Colors and Palettes
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-colorspace-lib = %{version}-%{release}
Requires: R-markdown
BuildRequires : R-dichromat
BuildRequires : R-ggplot2
BuildRequires : R-markdown
BuildRequires : R-mime
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R
BuildRequires : tcl

%description
CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB and polar CIELAB.
	     Qualitative, sequential, and diverging color palettes based on HCL colors
	     are provided along with corresponding ggplot2 color scales.
	     Color palette choice is aided by an interactive app (with either a Tcl/Tk
	     or a shiny GUI) and shiny apps with an HCL color picker and a
	     color vision deficiency emulator. Plotting functions for displaying
	     and assessing palettes include color swatches, visualizations of the
	     HCL space, and trajectories in HCL and/or RGB spectrum. Color manipulation

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
export SOURCE_DATE_EPOCH=1552729470

%install
export SOURCE_DATE_EPOCH=1552729470
rm -rf %{buildroot}
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
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library colorspace
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
R CMD check --no-manual --no-examples --no-codoc  colorspace || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/colorspace/CITATION
/usr/lib64/R/library/colorspace/DESCRIPTION
/usr/lib64/R/library/colorspace/INDEX
/usr/lib64/R/library/colorspace/LICENSE
/usr/lib64/R/library/colorspace/Meta/Rd.rds
/usr/lib64/R/library/colorspace/Meta/data.rds
/usr/lib64/R/library/colorspace/Meta/demo.rds
/usr/lib64/R/library/colorspace/Meta/features.rds
/usr/lib64/R/library/colorspace/Meta/hsearch.rds
/usr/lib64/R/library/colorspace/Meta/links.rds
/usr/lib64/R/library/colorspace/Meta/nsInfo.rds
/usr/lib64/R/library/colorspace/Meta/package.rds
/usr/lib64/R/library/colorspace/Meta/vignette.rds
/usr/lib64/R/library/colorspace/NAMESPACE
/usr/lib64/R/library/colorspace/NEWS.md
/usr/lib64/R/library/colorspace/R/colorspace
/usr/lib64/R/library/colorspace/R/colorspace.rdb
/usr/lib64/R/library/colorspace/R/colorspace.rdx
/usr/lib64/R/library/colorspace/cvdemulator/html/appInfo.html
/usr/lib64/R/library/colorspace/cvdemulator/html/info.html
/usr/lib64/R/library/colorspace/cvdemulator/prepareStaticContent.R
/usr/lib64/R/library/colorspace/cvdemulator/server.R
/usr/lib64/R/library/colorspace/cvdemulator/ui.R
/usr/lib64/R/library/colorspace/cvdemulator/www/cvdemulator.css
/usr/lib64/R/library/colorspace/cvdemulator/www/cvdemulator_darkmode.css
/usr/lib64/R/library/colorspace/cvdemulator/www/images/descimage.png
/usr/lib64/R/library/colorspace/cvdemulator/www/images/rainbow_desaturate.png
/usr/lib64/R/library/colorspace/cvdemulator/www/images/rainbow_deutan.png
/usr/lib64/R/library/colorspace/cvdemulator/www/images/rainbow_orig.png
/usr/lib64/R/library/colorspace/cvdemulator/www/images/rainbow_protan.png
/usr/lib64/R/library/colorspace/cvdemulator/www/images/rainbow_tritan.png
/usr/lib64/R/library/colorspace/data/Rdata.rdb
/usr/lib64/R/library/colorspace/data/Rdata.rds
/usr/lib64/R/library/colorspace/data/Rdata.rdx
/usr/lib64/R/library/colorspace/demo/brewer.R
/usr/lib64/R/library/colorspace/demo/carto.R
/usr/lib64/R/library/colorspace/demo/scico.R
/usr/lib64/R/library/colorspace/demo/viridis.R
/usr/lib64/R/library/colorspace/doc/colorspace.Rmd
/usr/lib64/R/library/colorspace/doc/colorspace.html
/usr/lib64/R/library/colorspace/doc/hcl-colors.R
/usr/lib64/R/library/colorspace/doc/hcl-colors.Rnw
/usr/lib64/R/library/colorspace/doc/hcl-colors.pdf
/usr/lib64/R/library/colorspace/doc/index.html
/usr/lib64/R/library/colorspace/hclcolorpicker/html/info.html
/usr/lib64/R/library/colorspace/hclcolorpicker/prepareStaticContent.R
/usr/lib64/R/library/colorspace/hclcolorpicker/server.R
/usr/lib64/R/library/colorspace/hclcolorpicker/ui.R
/usr/lib64/R/library/colorspace/hclcolorpicker/www/hclcolorpicker.css
/usr/lib64/R/library/colorspace/hclcolorpicker/www/hclcolorpicker_darkmode.css
/usr/lib64/R/library/colorspace/hclwizard/html/GrADS.html
/usr/lib64/R/library/colorspace/hclwizard/html/R.html
/usr/lib64/R/library/colorspace/hclwizard/html/RReg.html
/usr/lib64/R/library/colorspace/hclwizard/html/Register.html
/usr/lib64/R/library/colorspace/hclwizard/html/RegisterRcode.html
/usr/lib64/R/library/colorspace/hclwizard/html/colorplane.html
/usr/lib64/R/library/colorspace/hclwizard/html/info.html
/usr/lib64/R/library/colorspace/hclwizard/html/matlab.html
/usr/lib64/R/library/colorspace/hclwizard/html/python-example.html
/usr/lib64/R/library/colorspace/hclwizard/html/python.html
/usr/lib64/R/library/colorspace/hclwizard/prepareStaticContent.R
/usr/lib64/R/library/colorspace/hclwizard/server.R
/usr/lib64/R/library/colorspace/hclwizard/ui.R
/usr/lib64/R/library/colorspace/hclwizard/www/hclwizard.css
/usr/lib64/R/library/colorspace/hclwizard/www/hclwizard_darkmode.css
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_ag_grnyl.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_ag_sunset.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_berlin.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-red.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-red_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-red_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-yellow.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-yellow_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blue-yellow_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blues.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blues_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blues_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_blugrn.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_bluyl.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_bpy.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_brwnyl.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_bugn.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_bupu.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_burg.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_burgyl.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_cm.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_cold.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_cork.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_cyan-magenta.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_dark_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_dark_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_dark_mint.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_dynamic.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_emrld.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_gnbu.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_grays.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_green-brown.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_green-orange.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_green-yellow.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_greens.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_greens_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_greens_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_harmonic.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_heat.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_heat.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_heat_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_inferno.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_lajolla.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_light_grays.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_lisbon.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_magenta.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_mint.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_oranges.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_orrd.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_oryel.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_oslo.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_pastel_1.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_peach.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_pinkyl.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_plasma.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_pubu.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_pubugn.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purd.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purp.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purple-blue.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purple-brown.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purple-green.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purple-orange.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purples.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purples_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purples_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_purpor.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_rainbow.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_rdpu.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_red-blue.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_red-green.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_red-purple.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_red-yellow.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_redor.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_reds.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_reds_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_reds_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_set_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_set_3.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_sunset.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_sunsetdark.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_teal.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_tealgrn.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_terrain.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_terrain.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_terrain_2.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_tofino.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_topo.colors.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_tropic.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_turku.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_viridis.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_warm.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_ylgn.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_ylgnbu.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_ylorbr.png
/usr/lib64/R/library/colorspace/hclwizard/www/images/pal_ylorrd.png
/usr/lib64/R/library/colorspace/help/AnIndex
/usr/lib64/R/library/colorspace/help/aliases.rds
/usr/lib64/R/library/colorspace/help/colorspace.rdb
/usr/lib64/R/library/colorspace/help/colorspace.rdx
/usr/lib64/R/library/colorspace/help/paths.rds
/usr/lib64/R/library/colorspace/html/00Index.html
/usr/lib64/R/library/colorspace/html/R.css
/usr/lib64/R/library/colorspace/tests/Examples/colorspace-Ex.Rout.save
/usr/lib64/R/library/colorspace/tests/cvd.R
/usr/lib64/R/library/colorspace/tests/cvd.Rout.save
/usr/lib64/R/library/colorspace/tests/palettes.R
/usr/lib64/R/library/colorspace/tests/palettes.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/colorspace/libs/colorspace.so
/usr/lib64/R/library/colorspace/libs/colorspace.so.avx2
/usr/lib64/R/library/colorspace/libs/colorspace.so.avx512
