%define module pathspec

Name:		python-pathspec
Version:	1.0.3
Release:	1
Summary:	Utility library for gitignore style pattern matching of file paths.
URL:		https://pypi.org/project/pathspec/
License:	MPL-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(wheel)


%description
%{name} is a utility library for pattern matching of file paths.
So far this only includes Git's gitignore pattern matching.

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/pathspec
%{py_puresitedir}/pathspec*.*-info
