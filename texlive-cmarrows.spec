Name:		texlive-cmarrows
Version:	24378
Release:	2
Summary:	MetaPost arrows and braces in the Computer Modern style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/cmarrows
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmarrows.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmarrows.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This MetaPost package contains macros to draw arrows and braces
in the Computer Modern style.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/cmarrows/cmarrows.mp
%{_texmfdistdir}/metapost/cmarrows/rgbx0009.mp
%{_texmfdistdir}/metapost/cmarrows/rgbx0016.mp
%{_texmfdistdir}/metapost/cmarrows/rgbx0020.mp
%{_texmfdistdir}/metapost/cmarrows/rgbx0025.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0008.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0010.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0011.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0012.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0013.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0014.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0015.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0017.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0018.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0019.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0021.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0022.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0023.mp
%{_texmfdistdir}/metapost/cmarrows/sgbx0024.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0000.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0001.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0002.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0003.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0004.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0005.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0006.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0007.mp
%{_texmfdistdir}/metapost/cmarrows/tgbx0027.mp
%doc %{_texmfdistdir}/doc/metapost/cmarrows/README
%doc %{_texmfdistdir}/doc/metapost/cmarrows/cmarrows.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
