Name:		python-pathspec
Version:	0.12.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pathspec/pathspec-%{version}.tar.gz
Summary:	Utility library for gitignore style pattern matching of file paths.
URL:		https://pypi.org/project/pathspec/
License:	MPL 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Utility library for gitignore style pattern matching of file paths.

%files
%{py_puresitedir}/pathspec
%{py_puresitedir}/pathspec*.*-info
