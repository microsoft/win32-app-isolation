# Welcome to the Win32 Application Isolation repo
This repository contains the documentation and tools to help you create isolated Win32 applications. Win32 application isolation is a new security feature on Windows that helps contain the damage in the event an application is compromised. Win32 application isolation is built on the foundation of [AppContainers](https://learn.microsoft.com/en-us/windows/win32/secauthz/implementing-an-appcontainer), which offer a security boundary, and components that virtualize resources and provide brokered access to other resources.  

## Getting started 
* The first step to isolating your Win32 application is to package it to run isolated by following the instructions [here](docs/packaging/msix-packaging-tool.md). 
* Once you have your application packaged, use [Application Capability Profiler](docs/profiler/application-capability-profiler.md) to update the application to grant it access to additional resources.
* You're now ready to deploy and run your application on Windows.

Binaries for the tools used to package applications to run isolated are shared under the releases section of the repo.

Release notes for supported Windows builds and tools can be found [here](relnotes/RELEASE_NOTES.md).

## Communicating with the team
We'd love to hear your feedback and answer your questions! The best way to communicate with the team is through GitHub discussions and issues. Please search for similar discussions and issues before creating new ones. 

## Resources
You can find additional information about Win32 application isolation using the following resources: 
* [Coming Soon - Win32 Application Isolation Blog]()
* [Coming Soon - Win32 Application Isolation Build Session]()

## Contributing
If you would like to contribute to the documentation, please familiarize yourself with the Code of Conduct resources below and submit a pull request.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
