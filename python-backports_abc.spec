%global srcname backports_abc
%global sum A backport of recent additions to the 'collections.abc' module

Name:           python-%{srcname}
Version:        0.5
Release:        1
Summary:        %{sum}

License:        Python
URL:            https://pypi.python.org/pypi/backports_abc
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:	python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools

%description
%{sum}.

%package -n python2-%{srcname}
Summary:        %{sum}

%description -n python2-%{srcname}
%{sum}.


%prep
%setup -qn %{srcname}-%{version}
%apply_patches

cp -a . %py2dir

%build
python setup.py build
pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%buildroot
pushd %py2dir
python2 setup.py install --root=%buildroot

%check
%{__python2} setup.py test
%{__python3} setup.py test


%files -n python2-%{srcname}
%doc CHANGES.rst README.rst LICENSE
%{python2_sitelib}/*

%files 
%doc CHANGES.rst README.rst LICENSE
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}*.egg-info/
%{python3_sitelib}/__pycache__/*


%changelog
* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.5-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5-1
- Update to 0.5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-3
- Use %%{python3_pkgversion}

* Tue Feb 2 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-2
- Fix python3 package file ownership

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 0.4-1
- Initial package
