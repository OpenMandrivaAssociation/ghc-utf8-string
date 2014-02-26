%global debug_package %{nil}

%global module utf8-string

Summary:	Haskell UTF8-String library
Name:		ghc-utf8-string
Version:	0.3.7
Release:	2
License:	BSD
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
Patch0:		utf8-string-0.3.7-setup.patch
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
Requires(post,preun):	ghc

%description
A UTF8-String library for Haskell.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

