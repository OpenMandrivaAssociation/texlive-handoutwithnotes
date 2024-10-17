Name:		texlive-handoutwithnotes
Version:	62140
Release:	2
Summary:	Create Handouts with notes from your LaTeX beamer presentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/handoutwithnotes
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/handoutwithnotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/handoutwithnotes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/handoutwithnotes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides pgfpages layouts to place notes next to
the scaled slides.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/handoutwithnotes
%{_texmfdistdir}/tex/latex/handoutwithnotes
%doc %{_texmfdistdir}/doc/latex/handoutwithnotes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
