#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-googledrive
Version  : 2.0.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/googledrive_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/googledrive_2.0.0.tar.gz
Summary  : An Interface to Google Drive
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-gargle
Requires: R-glue
Requires: R-httr
Requires: R-jsonlite
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-pillar
Requires: R-purrr
Requires: R-rlang
Requires: R-tibble
Requires: R-uuid
Requires: R-vctrs
Requires: R-withr
BuildRequires : R-cli
BuildRequires : R-gargle
BuildRequires : R-glue
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-mockr
BuildRequires : R-pillar
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-uuid
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# googledrive <img src="man/figures/logo.png" align="right" height=140/>
<!-- badges: start -->

%prep
%setup -q -c -n googledrive
cd %{_builddir}/googledrive

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641029518

%install
export SOURCE_DATE_EPOCH=1641029518
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library googledrive
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library googledrive
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library googledrive
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc googledrive || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/googledrive/DESCRIPTION
/usr/lib64/R/library/googledrive/INDEX
/usr/lib64/R/library/googledrive/LICENSE
/usr/lib64/R/library/googledrive/Meta/Rd.rds
/usr/lib64/R/library/googledrive/Meta/features.rds
/usr/lib64/R/library/googledrive/Meta/hsearch.rds
/usr/lib64/R/library/googledrive/Meta/links.rds
/usr/lib64/R/library/googledrive/Meta/nsInfo.rds
/usr/lib64/R/library/googledrive/Meta/package.rds
/usr/lib64/R/library/googledrive/Meta/vignette.rds
/usr/lib64/R/library/googledrive/NAMESPACE
/usr/lib64/R/library/googledrive/NEWS.md
/usr/lib64/R/library/googledrive/R/googledrive
/usr/lib64/R/library/googledrive/R/googledrive.rdb
/usr/lib64/R/library/googledrive/R/googledrive.rdx
/usr/lib64/R/library/googledrive/R/sysdata.rdb
/usr/lib64/R/library/googledrive/R/sysdata.rdx
/usr/lib64/R/library/googledrive/WORDLIST
/usr/lib64/R/library/googledrive/doc/googledrive.Rmd
/usr/lib64/R/library/googledrive/doc/googledrive.html
/usr/lib64/R/library/googledrive/doc/index.html
/usr/lib64/R/library/googledrive/extdata/data/files_fields.csv
/usr/lib64/R/library/googledrive/extdata/data/mime_tbl.csv
/usr/lib64/R/library/googledrive/extdata/data/remote_example_files.csv
/usr/lib64/R/library/googledrive/extdata/data/translate_mime_types.csv
/usr/lib64/R/library/googledrive/extdata/example_files/chicken.csv
/usr/lib64/R/library/googledrive/extdata/example_files/chicken.jpg
/usr/lib64/R/library/googledrive/extdata/example_files/chicken.pdf
/usr/lib64/R/library/googledrive/extdata/example_files/chicken.txt
/usr/lib64/R/library/googledrive/extdata/example_files/imdb_latin1.csv
/usr/lib64/R/library/googledrive/extdata/example_files/r_about.html
/usr/lib64/R/library/googledrive/extdata/example_files/r_logo.jpg
/usr/lib64/R/library/googledrive/help/AnIndex
/usr/lib64/R/library/googledrive/help/aliases.rds
/usr/lib64/R/library/googledrive/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/googledrive/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/googledrive/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/googledrive/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/googledrive/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/googledrive/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/googledrive/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/googledrive/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/googledrive/help/figures/logo.png
/usr/lib64/R/library/googledrive/help/googledrive.rdb
/usr/lib64/R/library/googledrive/help/googledrive.rdx
/usr/lib64/R/library/googledrive/help/paths.rds
/usr/lib64/R/library/googledrive/html/00Index.html
/usr/lib64/R/library/googledrive/html/R.css
/usr/lib64/R/library/googledrive/secret/googledrive-docs.json
/usr/lib64/R/library/googledrive/secret/googledrive-testing.json
/usr/lib64/R/library/googledrive/tests/spelling.R
/usr/lib64/R/library/googledrive/tests/testthat.R
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/dribble.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_auth.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_cp.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_create.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_download.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_examples.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_fields.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_find.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_get.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_id-class.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_ls.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_mime_type.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_mv.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_publish.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_put.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_reveal.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_share.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_update.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/drive_upload.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/request_generate.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/shared_drives.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/shortcut.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/utils-paths.md
/usr/lib64/R/library/googledrive/tests/testthat/_snaps/utils-ui.md
/usr/lib64/R/library/googledrive/tests/testthat/driver.R
/usr/lib64/R/library/googledrive/tests/testthat/helper.R
/usr/lib64/R/library/googledrive/tests/testthat/setup-testing.R
/usr/lib64/R/library/googledrive/tests/testthat/test-camelCase.R
/usr/lib64/R/library/googledrive/tests/testthat/test-compat-dplyr.R
/usr/lib64/R/library/googledrive/tests/testthat/test-compat-vctrs.R
/usr/lib64/R/library/googledrive/tests/testthat/test-dribble.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_auth.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_cp.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_create.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_download.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_endpoints.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_examples.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_fields.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_find.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_get.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_get_path.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_id-class.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_link.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_ls.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_mime_type.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_mv.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_publish.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_put.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_read.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_reveal.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_rm.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_share.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_trash.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_update.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_upload.R
/usr/lib64/R/library/googledrive/tests/testthat/test-drive_user.R
/usr/lib64/R/library/googledrive/tests/testthat/test-files/client_secret_123.googleusercontent.com.json
/usr/lib64/R/library/googledrive/tests/testthat/test-files/just_a_dribble.rds
/usr/lib64/R/library/googledrive/tests/testthat/test-files/mix_of_files_and_teamdrives.rds
/usr/lib64/R/library/googledrive/tests/testthat/test-promote.R
/usr/lib64/R/library/googledrive/tests/testthat/test-request_generate.R
/usr/lib64/R/library/googledrive/tests/testthat/test-shared_drives.R
/usr/lib64/R/library/googledrive/tests/testthat/test-shortcut.R
/usr/lib64/R/library/googledrive/tests/testthat/test-utils-paths.R
/usr/lib64/R/library/googledrive/tests/testthat/test-utils-ui.R
/usr/lib64/R/library/googledrive/tests/testthat/test-utils.R
