%global tl_name handoutwithnotes
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Create Handouts with notes from your LaTeX beamer presentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/handoutwithnotes
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/handoutwithnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/handoutwithnotes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/handoutwithnotes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides pgfpages layouts to place notes next to the scaled
slides.

